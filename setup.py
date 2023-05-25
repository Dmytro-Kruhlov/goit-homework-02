from setuptools import setup


setup(name='sorte_by_DK',
      version='0.1.0',
      description='File sorter',
      url='http://github.com/dummy_user/useful',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': [
          'sorter = Goit_Homework_2.sort:sorter']}
      )
