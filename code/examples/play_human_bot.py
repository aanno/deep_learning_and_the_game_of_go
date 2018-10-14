import h5py
from dlgo.agent.predict import DeepLearningAgent, load_prediction_agent
from dlgo.httpfrontend import get_web_app

# tag::e2e_load_agent[]
model_file = h5py.File("../agents/deep_bot.h5", "r")
bot_from_file = load_prediction_agent(model_file)

web_app = get_web_app({'predict': bot_from_file})
web_app.run(host='0.0.0.0')
# end::e2e_load_agent[]
