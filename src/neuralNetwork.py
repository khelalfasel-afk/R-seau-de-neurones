import numpy as np

class NeuralNetwork :
    
    def __init__(self,inputNmbr,hiddenLayersNmbr,outputNmbr):
        
        #weights initialization
        self.weightsTab = []
        length = len(hiddenLayersNmbr)
        if  length == 0:
            self.weightsTab.append(np.random.rand(inputNmbr,outputNmbr ))
        else:
            self.weightsTab.append(np.random.rand(inputNmbr,hiddenLayersNmbr[0])* 10 - 5)
            for i in range(1,length): 
                self.weightsTab.append(np.random.rand(hiddenLayersNmbr[i-1],hiddenLayersNmbr[i]) * 10 - 5)
            self.weightsTab.append(np.random.rand( hiddenLayersNmbr[length-1],outputNmbr)* 10 - 5)

        #biases initialization 
        self.biasTab = []
        for i in range(length):
            self.biasTab.append(np.random.rand(hiddenLayersNmbr[i]))
        self.biasTab.append(np.random.rand(outputNmbr))

    def forward(self, inputs):
            length = len(self.weightsTab)
            inputs = np.array(inputs)
            outputvalues = inputs.T @ self.weightsTab[0] + self.biasTab[0]
            outputvalues = self.sigmoid(outputvalues)

            if length > 1 :
                for i in range(1,length):
                    outputvalues = outputvalues @ self.weightsTab[i] + self.biasTab[i]
                    outputvalues = self.sigmoid(outputvalues)

            return outputvalues 

    def Relu(self, inputs):
        outputs = np.maximum(0, inputs)
        return outputs 
    
    def sigmoid(self, inputs):
        outputs = 1 / (1 + np.exp(-inputs))
        return outputs