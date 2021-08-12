class Model:
    '''
    Model class
    This class setup a deep learning model have train to predict image
    '''
    
    # import lib
    import Config.reader as reader
    import numpy

    def predict(self, image):
        model = self.reader.Reader().get_model()
        return model.predict(self.numpy.expand_dims(image, 0))