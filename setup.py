from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()
setup(name='autolike',
      version='0.0.2',
      description='Automatically like any given Facebook URL if the user is logged in.',
      long_description=readme(),
      install_requires=['pymsgbox', 'PyTweening>=1.0.1', 'Pillow', 'pyscreeze', 'pyautogui'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License'
      ],
      keywords='Facebook fb like liker autolike autoliker automation',
      url='http://github.com/arsho/autolike',
      author='Ahmedur Rahman Shovon',
      author_email='shovon.sylhet@gmail.com',
      license='BSD',
      packages=['autolike'],
      package_data={'autolike': ['autolike/*.png']},
      include_package_data=True,
      zip_safe=False)
