from locust import HttpLocust, TaskSet


class FileServiceBehavior(TaskSet):
    def on_start(self):
        self.upload()

    @task
    def upload(self):
        ''' File service upload test '''
        pass

class PolicyService(HttpLocust):
    task_set = FileServiceBehavior
    min_wait = 5000
    max_wait = 9000
