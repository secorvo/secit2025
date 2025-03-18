# Übung zu Secure Supply Chain

Die folgenden Übungsteile dienen dazu, praktisch in das Thema [_Software Bill of Material (SBOM)_](https://www.cisa.gov/sbom) einzuführen.

## Übungen mit [syft](https://github.com/anchore/syft)

Die Übungen sollen mit syft als Docker-Container durchgeführt werden. Alternativ kann syft auch installiert werden. 

### Fähigkeiten von syft

> **AUFGABE:** Diskutiert welche Quellen syft analysieren kann und welche Ausgaben es erzeugen kann.

### Lokaler Docker Container

> **AUFGABE:** Erzeuge mit syft ein SBOM eines lokalen Docker Containers im Format CycloneDX-JSON und eines im Format CycloneDX-XML.

### Source Code Repository

> **AUFGABE:** Erzeuge mit syft ein SBOM des Source Codes von [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) in einem beliebigen Format.

### Analyse CycloneDX JSON mit jq

> **AUFGABE:** Analysiere mit jq die erste erzeugte CycloneDX-JSON-Datei.
> Du könntest bspw. die Datei formatiert ausgeben und eine Liste von Pakten mit Lizenzen ausgeben.

## Übungen mit [grype](https://github.com/anchore/grype)

Die Übungen sollen mit grype als Docker-Container durchgeführt werden. Alternativ kann grype auch installiert werden. 

### Fähigkeiten von grype

> **AUFGABE:** Diskutiert welche Quellen grype analysieren kann und welche Ausgaben es erzeugen kann.

### SBOM Analyse

> **AUFGABE:** Analysiert mit grype ein vorher erstellen SBOM.

### Container Analyse

> **AUFGABE:** Analysiert mit grype ein Docker Image.

## Übungen mit [trivy](https://github.com/aquasecurity/trivy)

Die Übungen sollen mit trivy als Docker-Container durchgeführt werden. Alternativ kann trivy auch installiert werden. 

### Fähigkeiten von syft

> **AUFGABE:** Diskutiert welche Quellen trivy analysieren kann und welche Ausgaben es erzeugen kann.

### Container Analyse

> **AUFGABE:** Analysiert mit trivy das Docker Image python:latest.

### SBOM Analyse

> **AUFGABE:** Analysiert mit trivy ein vorher erstellen SBOM.

### Source Code Repository

> **AUFGABE:** Erzeuge mit trivy ein SBOM des Source Codes von [OWASP Juice Shop](https://github.com/juice-shop/juice-shop).

## Übungen mit [OWASP Dependency Track](https://github.com/DependencyTrack)

OWASP Dependency Track ist vorinstalliert. Log Dich auf dem Deskmate-Rechner unter [http://localhost:8088](http://localhost:8088) (oder bspw. [http://secit-deskmate:8088](http://secit-deskmate:8088) mit Tailscale auf dem eigenen Client) mit den Default-Credentials (_admin/admin_) ein und ändere das Passwort.

### Fähigkeiten von Dependency Track

> **AUFGABE:** Diskutiert wozu Dependency Track dienen soll.

### Projekt anlegen

> **AUFGABE:** Lege für OWASP Juice Shop in Dependency Track ein Projekt an.

### Ermittle API Key und Projekt ID

> **AUFGABE:** Ermittle als Vorbereitung für die nächste Aufgabe in der Weboberfläche den API Key und die Projekt ID.

### Hochladen SBOM in Dependency Track

> **AUFGABE:** Versuche eine Juice Shop SBOM per API zu Dependency Track hochzuladen (in der bundled Version ist die URL `http://localhost:8088/api/v1/bom`).
> Sollte das nicht funktionieren, lade sie über die Weboberfläche hoch.

### Analyse von Projekt in Dependency Track

> **AUFGABE:** Stoße eine Analyse von OWASP Juice Shop in der Weboberfläche von Dependency Track an.




