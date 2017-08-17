from locust import HttpLocust, TaskSet, task

'''
pip install locustio
http://www.cnblogs.com/walker-dead-cave/p/5770200.html
'''
class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/index")

    @task
    def about(self):
        self.client.post("/about")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 3000
