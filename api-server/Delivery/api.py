

class API:
    '''
    API class:
    Manufacturing api function
    '''

    # Import lib
    import Delivery.message as message
    import Application.app as app
    import json
    import flask
    import base64
    import numpy
    import cv2 
    from PIL import Image
    import io
    import matplotlib.pyplot as plt

    def ping(self):
        '''
        This function will check that if this service is good runnable
        '''

        try:
            return self.message.Message().buildMessage("pong")
        except:
            return self.message.Message().buildErrorMessage("ping function have error")

    def chestClassify(self):
        '''
        This function will prepare images and give to handler function to classify chest
        Parameter:
            images: a set of chest image
        Return:
            a set of result classifier belong the set of the chest image
        '''

        try:
            # Convert json data to distionary
            contents = self.json.loads(self.flask.request.data)

            # Identity a set of chest image
            results = []

            for image in contents['images']:
                # Convert base64 image
                img = self.Image.open(
                            self.io.BytesIO(
                                self.base64.b64decode(
                                    image['data']
                                )
                            )
                        ).convert('RGB')

                percen = self.app.App().chestPredict(img)

                # Init result set
                result = {}
                result['id'] = image['id']
                result['pneumonia'] = float(percen)

                results.append(result)

            json_results = self.json.dumps(results)

            return self.message.Message().buildMessage(json_results)
        except:
            return self.message.Message().buildErrorMessage("chest classify function have error")
    # def graphRelativeCompute():
    #     try:
    #         content = json.loads(flask.request.data)
    #         log = app.computeRelativeGraph(content)

    #         if log != None:
    #             return message.buildMessage(log)
    #             # return message.buildMessage("OK")

    #         return message.buildMessage("No result")
    #     except:
    #         return message.buildErrorMessage("graphRelativeCompute func have error")