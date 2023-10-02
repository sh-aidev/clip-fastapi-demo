from locust import HttpUser, task, between

class StressTest(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_text_endpoint(self):
        files = {'file': open('images/dog.png', 'rb')}
        url = "/image-to-text?text=an image of a dog, image of a cat"
        res=self.client.post(url,files=files)