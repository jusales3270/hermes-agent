#!/usr/bin/env python3
import sys, json, urllib.request

def main():
    if len(sys.argv) < 4:
        print("uso: registrar_alerta.py <severity> <title> <description> [department]")
        sys.exit(1)

    severity = sys.argv[1]
    title = sys.argv[2]
    description = sys.argv[3]
    department = sys.argv[4] if len(sys.argv) > 4 else "geral"

    dados = {
        "severity": severity,
        "title": title,
        "description": description,
        "source": "Sara (monitor)",
        "department": department,
    }

    req = urllib.request.Request(
        "http://dashboard:3000/api/alerts",
        data=json.dumps(dados).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        resp = urllib.request.urlopen(req, timeout=10).read().decode()
        print(resp)
    except Exception as e:
        print(f"ERRO ao registrar alerta: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
