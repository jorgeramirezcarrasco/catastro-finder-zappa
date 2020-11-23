# Catastro Finder Zappa

Catastro Finder as server-less, event-driven python application

---

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Remember to have the credentials in ~/.aws/credentials

Deploy

```bash
zappa deploy dev
```

Update

```bash
zappa update dev
```

Delete

```bash
zappa undeploy dev
```
