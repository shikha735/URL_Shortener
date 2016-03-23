from cx_Freeze import setup, Executable

setup(name='URL Shortener',
      version='1',
      description='shortens the URLs',
      executables= [Executable("main.py")]
      )
