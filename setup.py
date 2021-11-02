import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name='x_control',
  version='0.0.0',
  author='Zeffiretti Hiesh',
  author_email='hiesh@mail.com',
  description='Smuro Robotics Caculation Package',
  long_description=long_description,
  long_description_content_type="text",
  url='https://github.com/zeffiretti/x-control',
  project_urls={
    "Bug Tracker": "https://github.com/zeffiretti/x-control/issues"
  },
  license='MIT',
  packages=['x_control'],
  install_requires=['time', 'warnings'],
)
