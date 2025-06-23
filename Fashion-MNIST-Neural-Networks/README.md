📊 Fashion-MNIST Neural Network Experiments

In this project I implement and compare both fully-connected neural networks (NNs) and convolutional neural networks (CNNs) to classify the Fashion-MNIST dataset (70 000 grayscale 28 × 28 images of 10 clothing categories). Key aspects include:

- **Model types**  
  - Simple NN: one or more dense layers with configurable hidden sizes  
  - CNN: stacks of Conv → ReLU → Pooling blocks, with adjustable depth and filter sizes  

- **Optimizers tested**  
  - Stochastic Gradient Descent (with momentum)  
  - Adam  
  - RMSprop  

- **Regularization techniques**  
  - Dropout (rates from 0.2 to 0.5)  
  - L1 and L2 weight penalties  

- **Topology experiments**  
  - Varying number of convolutional blocks (2–4)  
  - Small (3×3) vs larger (5×5) kernels  
  - Channel depths (32→64→128, etc.)  

All data is loaded from CSV files (`train.csv` / `test.csv`), preprocessing scales pixel values to [0,1], and results (accuracy, loss curves, confusion matrices) are tracked for each configuration. The accompanying notebook walks through EDA, model definitions, training loops, and evaluation.
