!pip install tflite2onnx

import tflite2onnx

tflite_path = 'model_name.tflite'
onnx_path = 'model_name.onnx'

tflite2onnx.convert(tflite_path, onnx_path)