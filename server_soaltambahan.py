import socket
import os

def send_file(conn, filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
            conn.sendall(data)
        print(f"File {filename} berhasil dikirim")
    except FileNotFoundError:
        conn.sendall(b"File tidak ditemukan")

def receive_file(conn, filename, folder):
    try:
        filepath = os.path.join(folder, filename)
        if os.path.exists(filepath):
            # Jika file sudah ada, tambahkan angka unik ke nama file
            filename, extension = os.path.splitext(filename)
            counter = 1
            while os.path.exists(os.path.join(folder, f"{filename}_{counter}{extension}")):
                counter += 1
            filename = f"{filename}_{counter}{extension}"
            filepath = os.path.join(folder, filename)
        with open(filepath, 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"File {filename} (ukuran: {get_file_size(filepath)}) berhasil diterima")
    except:
        print("Terjadi kesalahan saat menerima file")

def remove_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} berhasil dihapus")
    except FileNotFoundError:
        print("File tidak ditemukan")
    except:
        print("Terjadi kesalahan saat menghapus file")

def list_files():
    files = os.listdir('.')
    return '\n'.join(files)

def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        size_mb = size / (1024 * 1024)
        return f"{size_mb:.2f} MB"
    except FileNotFoundError:
        return "File tidak ditemukan"
    except:
        return "Terjadi kesalahan saat mendapatkan ukuran file"

def process_command(command, conn, folder):
    if command.startswith("ls"):
        return list_files()
    elif command.startswith("rm"):
        filename = command.split(" ")[1]
        remove_file(filename)
    elif command.startswith("download"):
        filename = command.split(" ")[1]
        send_file(conn, filename)
    elif command.startswith("upload"):
        filename = command.split(" ")[1]
        receive_file(conn, filename, folder)
    elif command.startswith("size"):
        filename = command.split(" ")[1]
        return get_file_size(filename)
    elif command.startswith("byebye"):
        return "byebye"
    elif command.startswith("connme"):
        return "connme"
    else:
        return "Perintah tidak valid"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Menunggu koneksi...")

    folder = "received_files"  # Folder tempat file diterima

    while True:
        conn, addr = server_socket.accept()
        print(f"Terhubung dengan {addr}")

        while True:
            command = conn.recv(1024).decode()
            if not command:
                break

            result = process_command(command, conn, folder)
            if result == "byebye":
                conn.sendall(b"Terima kasih! Sampai jumpa.")
                break
            elif result == "connme":
                conn.sendall(b"Terhubung kembali.")
            else:
                conn.sendall(result.encode())

        conn.close()
        print("Koneksi ditutup")

if __name__ == "__main__":
    main()
