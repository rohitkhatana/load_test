from locust import HttpLocust, TaskSet, task


class FileServiceBehavior(TaskSet):
    def on_start(self):
        self.upload()

    @task
    def upload(self):
        ''' File service upload test '''
        file_info = {'file': ('some.pdf', open('/Users/rohitkhatana/Downloads/2312100174779600000.pdf', 'rb'), "application/pdf")}
        values = {'bucketName': 'bucket', 'host': 'localhost', 'path': 'load_test'}
        #self.client.post('/v1/policy/AEX6BVWJ7D4/upload', files=file_info, data=values)
        self.client.post('/v1/file/upload', files=file_info, data=values)

    def download(self):
        pass

class PolicyService(HttpLocust):
    task_set = FileServiceBehavior
    min_wait = 5000
    max_wait = 9000
