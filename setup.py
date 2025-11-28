from setuptools import setup, Extension

module = Extension("prime", sources=["prime_module.c"])

setup(
    name="prime",
    version="1.0",
    ext_modules=[module],
)
