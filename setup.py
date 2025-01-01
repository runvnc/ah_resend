from setuptools import setup, find_packages

setup(
    name="ah_resend",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[
        "resend",
        "pydantic"
    ],
    author="MindRoot",
    author_email="info@mindroot.ai",
    description="Resend.com email service integration for MindRoot",
    keywords="email, resend, mindroot",
    python_requires=">=3.9"
)