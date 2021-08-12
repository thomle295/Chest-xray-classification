class Reader:
    '''
    Reader class
    '''
    # Import library
    import yaml
    import tensorflow.keras as keras

    # Identify path config file 
    config_dir = "Config/config.yaml"

    def get_config(self):
        '''
        This function try to read a config file have identity above;
        Giving the value of the config file
        '''

        # Read config file
        with open(self.config_dir) as file:
            # Load config data
            data = self.yaml.load(file, Loader=self.yaml.FullLoader)

            # Close file
            file.close()
        
        return data

    def get_model(self):
        '''
        This function get model have train
        Return a model
        '''

        return self.keras.models.load_model("Config/model.h5")