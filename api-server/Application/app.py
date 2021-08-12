class App:
    '''
    App class
    Manufacturing application function of this service
    '''

    import cv2
    import Config.reader as reader
    import Infrastructure.model as model
    import numpy

    def chestPredict(self, image):
        # self.cv2.imshow("image", image)

        config = self.reader.Reader().get_config()

        resize_image = image.resize(
            (
                config['MODEL']['IMAGE_INPUT_HEIGHT_SIZE'],
                config['MODEL']['IMAGE_INPUT_WIDTH_SIZE']
            )
        )

        result = self.model.Model().predict(self.numpy.array(resize_image))
        return round(result[0][1], 3)
