from setuptools import setup, find_packages

setup(
    name="image_processing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "opencv-python",  
        "numpy"
    ],
    description="A simple image processing package.",
    author="Edivan Carvalho",
    author_email="",
    url="https://github.com/EdivanCarvalho1/projeto-python",
)
