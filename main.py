from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """ Класс для обработки запросов."""
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        path = self.get_path()
        print(path)
        try:
            with open(path, "r", encoding="utf-8") as file:
                page_content = file.read()
                self.send_response(200)  # Отправка кода ответа
                self.send_header("Content-Type", "text/html; charset=utf-8")  # Отправка типа данных, который будет передаваться
                self.end_headers()  # Завершение формирования заголовков ответа
                self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа
        except FileNotFoundError:
            self.send_error(404, "File Not Found")

    def get_path(self):
        if self.path == "/":
            return "contacts.html"
        return self.path


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
