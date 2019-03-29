### Using this project

For creating a TF dash django app, you must first create the TFDashModel under dash_tf.configuration.TFDashModel

Create ModelInputs and ModelOutputs then pass a list of these to the TFDashModel

For inputting, set the values of the ModelInputs using 'set_value()' then run the simulation
using TFDashModel.run()