import setuptools

setuptools.setup(
    name="streamlit-vega-lite",
    version="0.0.1",
    author="Dominik Moritz",
    author_email="",
    description="",
    long_description="A Vega-Lite Component for Streamlit that Supports Selections",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
