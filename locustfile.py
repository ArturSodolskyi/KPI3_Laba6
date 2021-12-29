from locust import HttpUser, task, between

class User(HttpUser):

    host = 'https://reqres.in/api'
    time = between(1, 5)


    @task(1)
    def GetUser(self):
        self.client.get("/users/4")

    @task(2)
    def AddUser(self):
        self.client.post("/users", json={
            "email": "arturTest1@reqres.in",
            "password": "Test123!"
        })

    @task(1)
    def UpdateUser(self):
        self.client.patch("/users", json={
            "email": "arturTest1@reqres.in",
            "password": "Test12345!"
        })

    @task(3)
    def RegisterUser(self):
        self.client.post("/users", json={
            "email": "arturtest@reqres.in",
            "password": "Test123!"
        })

    @task(3)
    def LoginUser(self):
        self.client.post("/users", json={
            "email": "arturtest@reqres.in",
            "password": "Test123!"
        })

    @task(1)
    def DeleteUser(self):
        self.client.delete("/users/4")