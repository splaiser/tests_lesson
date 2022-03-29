import requests, unittest, config
from api import YaUploader


class TestApi(unittest.TestCase):

    def test_YaUploader_get_new_folder(self):   # Тест на создание папки
        test_uploader = YaUploader(config.TOKEN)
        response = test_uploader.get_new_folder("netology")
        self.assertEqual(response, 201)

    def test_YaUploader_get_new_folder_2(self):  # Тест на создание папки, если папка уже создана
        test_uploader = YaUploader(config.TOKEN)
        response = test_uploader.get_new_folder("netology")
        self.assertEqual(response, 409)

    def test_YaUploader_get_file_info(self):    # Тест папка уже создана
        test_uploader = YaUploader(config.TOKEN)
        response = test_uploader.get_file_info("netology")
        self.assertEqual(response, 200)

    def test_YaUploader_get_file_info_2(self):    # Тест папки не существует
        test_uploader = YaUploader(config.TOKEN)
        response = test_uploader.get_file_info("netology")
        self.assertEqual(response, 404)


if __name__ == '__main__':
    unittest.main()
