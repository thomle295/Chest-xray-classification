class Message:
    '''
    Message class:
    Prepare message before delivery
    '''

    # import lib
    import time
    import json

    # Initialize message
    message = {}

    def buildMessage(self, data):
        '''
        This function sparse data to json \n
        Parameter:
            data: the data that you want to delivery
        Return:
            json data that has sparsed
        '''

        self.message['returncode'] = 1
        self.message['data'] = data
        self.message['timestamp'] = self.time.time()
        return self.json.dumps(self.message)

    def buildErrorMessage(self, err):
        '''
        This function sparse data to json (error messeage) \n
        Parameter:
            data: the data that you want to delivery
        Return:
            json data that has sparsed
        '''

        self.message['returncode'] = -1
        self.message['data'] = err
        self.message['timestamp'] = self.time.time()
        return self.json.dumps(self.message)