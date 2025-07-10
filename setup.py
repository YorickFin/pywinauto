from setuptools import setup, find_packages

setup(
    name="pywinauto",
    version="0.1.0",
    author="YorickFin",
    author_email="1582456060@qq.com",
    license="GPLv3",    # 项目的许可证
    url = "https://github.com/YorickFin/pywinauto",  # 项目主页
    description="Python library for automating Windows",    # 包的简短描述
    long_description = open("README.md", encoding="utf-8").read(),  # 包的详细描述，通常来自README文件
    long_description_content_type = "text/markdown",  # README文件的格式

    packages = find_packages(exclude = ["examples"]),  # 自动找到所有包
    install_requires=[],    # 依赖项列表
    classifiers=[   # 项目的分类信息
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires='>=3.6',    # Python版本要求
    zip_safe=False,            # 不使用压缩包安装
)