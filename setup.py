from setuptools import setup


setup(name='clean_folder',
      version='0.1.0',
      description='File sorter',
      url='https://github.com/Dmytro-Kruhlov/goit-homework-02',
      author='Dmytro Kruhlov',
      author_email='hazzy1451@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': [
          'clean-folder = clean_folder.sort:main']}
      )
