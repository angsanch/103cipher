# 103cipher

Mathematical message masking and multiplying matrices.

Project for semester 1 of the Epitech Math module.

### Description

This project implements a matrix-based ciphering software. The encryption process involves:
- Translating the key into numbers using the ASCII table.
- Converting the numbered key into a square matrix.
- Translating the clear message into numbers using the ASCII table.
- Converting the numbered message into a matrix with columns fitting the key matrix size.
- Multiplying the two matrices to get the encrypted message.

Decryption is the reverse process, requiring the inversion of the key matrix. Inverting larger matrices is a bonus task.

## Getting Started

### Dependencies

- [Python3](https://python.org/)

### Installation

* Download/Clone the repository and enter its directory
* Now you are ready to run the code

## Usage

**Execution:** `./103cipher message key flag`

### Arguments
- **`message`**: The message to be encrypted or decrypted, made of ASCII characters.
- **`key`**: The encryption key, made of ASCII characters.
- **`flag`**: `0` for encryption, `1` for decryption.

### Examples

To encrypt a message:
```
$> ./103cipher "Just because I don't care doesn't mean I don't understand." "Homer S" 0
Key matrix:
72 111 109
101 114 32
83 0 0
Encrypted message:
26690 21552 11810 19718 16524 13668 25322 22497 14177 28422 26097 16433 12333 11874 5824 27541 23754 14452 17180 17553 7963 26387 22047 13895 18804 14859 12033 27738 23835 15331 21487 16656 13238 21696 15978 6976 20750 23307 14093 16788 11751 8981 22339 24861 15619 21295 16524 13668 26403 23610 15190 29451 25764 16106 26394 23307 14093 3312 5106 5014
```

To decrypt a message:
```
$> ./103cipher "26690 21552 11810 19718 16524 13668 25322 22497 14177 28422 26097 16433 12333 11874 5824 27541 23754 14452 17180 17553 7963 26387 22047 13895 18804 14859 12033 27738 23835 15331 21487 16656 13238 21696 15978 6976 20750 23307 14093 16788 11751 8981 22339 24861 15619 21295 16524 13668 26403 23610 15190 29451 25764 16106 26394 23307 14093 3312 5106 5014" "Homer S" 1
Key matrix:
0.0 0.0 0.012
-0.004 0.012 -0.012
0.013 -0.013 0.004
Decrypted message:
Just because I don't care doesn't mean I don't understand.
```

## Acknowledgments

* [Epitech](https://www.epitech.eu/)

## Authors

* **Daniel Sanchez** ([GitHub](https://github.com/angsanch) / [LinkedIn](https://www.linkedin.com/in/angeldanielsanchez/))
* **Xinru Xu** ([GitHub](https://github.com/Exinru) / [LinkedIn](https://www.linkedin.com/in/xinru-xu/))

## License

This project is licensed under the GNU Public License version 3.0 - see the [LICENSE](LICENSE) file for details.
