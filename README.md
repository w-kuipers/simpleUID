# simpleUID (unique ID) for Python

[![GitHub releases](https://img.shields.io/github/v/release/w-kuipers/simpleUID)](https://github.com/w-kuipers/simpleUID/releases)
[![PyPI release](https://img.shields.io/pypi/v/simpleUID.svg)](https://pypi.org/project/simpleUID/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple and intuitive Python package for generating unique IDs.

This package helps developers by bringing them some "quality of life" features. Stop rewriting the same piece of code in every project.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#install-using-pip">Install using PIP</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#support">Support</a></li>
    <li><a href="#maintainer">Maintainer</a></li>
    <li><a href="#contributing">Contibruting</a></li>
    <li><a href="#license">License</a></li>

  </ol>
</details>

## Installation

### Install using PIP

    pip install simpleUID

Note the `pip` refers to the Python 3 package manager. In environment where Python 2 is also available the correct command may be `pip3`.

## Usage

For a more detailed explaination, visit the [documentation](https://github.com/w-kuipers/simpleUID/wiki).

Import simpleUID:

    import simpleUID

Create a random string:

    simpleUID.string()

You can specify the string length and a prefix:

    simpleUID.string(length=20, prefix='start')

All functions are:
Function        | Functionality 
------------- | -----
[string](https://github.com/w-kuipers/simpleUID/wiki/usage#string)       | Generates a random string. 
[integer](https://github.com/w-kuipers/simpleUID/wiki/usage#integer) | Generates a random integer. 
[password](https://github.com/w-kuipers/simpleUID/wiki/usage#password)  |   Generates an alphanumeric password with at least one lowercase character, at least one uppercase character, and at least three digits. |
[bytes](https://github.com/w-kuipers/simpleUID/wiki/usage#bytes)   |  Generates a random byte string. 
[hex](https://github.com/w-kuipers/simpleUID/wiki/usage#hex)   |  Generates a random byte string. 
[urlsafe](https://github.com/w-kuipers/simpleUID/wiki/usage#urlsafe)   |  Generates a random byte string. 
[database](https://github.com/w-kuipers/simpleUID/wiki/usage#database)  | Generates a random ID using the `string` or `integer` functions, then it checks it's uniqueness against database. 

Keep in mind that the prefix for the `integer` function should be of type `int`.

#### Cursor
Currently only the [mysql-connector](https://pypi.org/project/mysql-connector/) cursor object has been tested to work with this package. If you encounter issues with other cursor objects, please [create an issue](https://github.com/w-kuipers/simpleUID/issues) on GitHub. 
The cursor argument should be a dictionairy structured like the example below:

    cursor = {
        "cursor": cursor, ## Currently only tested with MYSQL
        "table": "table_name",
        "column": "column_name"
    }

### Max Length
The default maximum length has been set to 1000. This is to prevent unnecessary use of hardware power. If for some reason this should be ignored, set `ignore_max_length` to `True`.

## Support

If you found a problem with the software, please [create an issue](https://github.com/w-kuipers/simpleUID/issues) on GitHub.

## Maintainer

This project is maintained by [Wibo Kuipers](https://github.com/w-kuipers).

## Contributing

Your contributions are highly appreciated. Please [create a pull request](https://github.com/w-kuipers/simpleUID/pulls) on GitHub. Bigger changes need to be discussed with the development team via the [issues section at GitHub](https://github.com/w-kuipers/simpleUID/issues) first.


## License

[MIT LICENSE](https://github.com/w-kuipers/simpleUID/blob/master/LICENSE)
