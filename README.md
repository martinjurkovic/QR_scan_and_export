QR_scan_and_export
==============================

Scan QR code from an image and export it to SVG.

Getting Started
------------
Install requirements: `pip install -r requirements.txt`

Run script:
`python main.py {flags}`

Flags: 
* (required) `-fp`, `--filepath`: Path to image with QR code
* (optional) `-qrv`: `--qrversion`, Version of QR code (from 1-40), type int
* (optional) `-et`: `--exporttype`, File type of exported qr code (svg, jpg, png...)
