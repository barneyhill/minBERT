from setuptools import setup

setup(name='minBERT',
      version='0.0.1',
      author='Andrej Karpathy',
      packages=['minbert'],
      description='A PyTorch re-implementation of BERT',
      license='MIT',
      install_requires=[
            'torch',
      ],
)
