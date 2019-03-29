import tensorflow as tf


class TfDashModel(object):

    def __init__(self, inputs, outputs, tf_model_path):
        assert type(inputs) is list, "The model inputs must be given in a list"
        assert type(outputs) is list, "The model outputs must be given in a list"
        assert type(inputs[0]) is ModelInput, "The inputs must be of type ModelInput"
        assert type(outputs[0]) is ModelOutput, "The inputs must be of type ModelOutput"
        # assert type(tf_model) is

        # now save the init values
        self.inputs = inputs
        self.outputs = outputs
        self.tf_model = tf_model_path

    # run the tf model and give to the dash-django app
    def run(self):
        self.tf_model


# arbitrary model parameters
class ModelParameter(object):

    def __init__(self, name, tensor, unit):
        self.name = name
        self.tensor = tensor
        self.unit = unit
        self.value = None


# a model input
class ModelInput(ModelParameter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # input to the model
    def set_value(self, value, unit):
        assert self.unit is unit, "Your unit was {0} but it should be {1}".format(unit, self.unit)

        # save the value
        self.value = value


# a model output
class ModelOutput(ModelParameter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

