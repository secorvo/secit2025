# Hinweise zu Secure-Software-Supply-Chain

## Docker Images

Übersicht über Docker Images:

```bash
docker image ls
```

## [syft](https://github.com/anchore/syft)

### Erzeugen eines SBOM aus einem lokalen Docker-Containers

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ./out:/out --name Syft anchore/syft:latest docker:bkimminich/juice-shop -o cyclonedx-xml=/out/juice_shop.xml
```

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ./out:/out --name Syft anchore/syft:latest docker:bkimminich/juice-shop -o cyclonedx-json=/out/juice_shop.json
```

### Erzeugen eines SBOM aus einem Source-Projekt

```bash
git clone https://github.com/juice-shop/juice-shop.git
cd juice-shop
```

```bash
docker run --rm -v $(pwd):/project anchore/syft:latest dir:/project -o json > juice_shop_github.json
```

## Anschauen und Filtern eine JSON-SBOM mit `jq`

Komplette SBOM:

```bash
jq . ./out/juice_shop.json
```

Pakete mit Lizenzen:

```bash
jq '.components[] | {name: .name, version: .version, licenses: .licenses[]?.license.id}' ./out/juice_shop.json
```

Pakete ohne Lizenzen:

```bash
 jq '.components[] | select(.licenses == null) | {name: .name, version: .version}' ./out/juice_shop.json
```


## [grype](https://github.com/anchore/grype)

```bash
docker run --rm -v ./out:/out --name Grype anchore/grype:latest sbom:/out/juice_shop.json
```

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock --name Grype anchore/grype:latest docker:bkimminich/juice-shop 
```

## [trivy](https://trivy.dev/latest/)

[trivy Documentation](https://trivy.dev/latest/docs/)
[trivy Github Repo](https://github.com/aquasecurity/trivy)

Scan Python Image

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock -v ./trivy_cache:/root/.cache/ aquasec/trivy:latest image python:latest
```

Scan OWASP Juice Shop SBOM:

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock -v ./trivy_cache:/root/.cache/ -v ./out:/out aquasec/trivy:latest sbom /tmp/juice_shop.json
```

Scan OWASP Juice Shop Source:

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock -v .:/src aquasec/trivy:latest fs --scanners vuln,config,secret /src
```

## OWASP Dependency Track

[Dependency Track Github Repo](https://github.com/DependencyTrack)
[Dependency Track Homepage](https://dependencytrack.org)

### Installation (optional da vorinstalliert als [Bundled Image](https://hub.docker.com/r/dependencytrack/bundled))

```bash
curl -LO https://dependencytrack.org/docker-compose.yml
docker-compose up -d
```

### Upload eines SBOM via API

Beispiel:

```bash
# IDs und API-Key müssen angepasst werden!
export JUICE_SHOP_PROJECT_ID=31cc8a9d-03fe-4695-9762-113b3adff6c1

export DT_SBOM_FILE=./out/juice_shop.json
export DT_API_KEY=odt_IXQqoZ6ynV06lDTPIPSDze7IDquM1b6N
export DT_PROJECT_ID=$JUICE_SHOP_PROJECT_ID

curl -X "POST" "http://localhost:8088/api/v1/bom" -H 'Content-Type: multipart/form-data' -H "X-Api-Key: $DT_API_KEY" -F "project=$DT_PROJECT_ID" -F "bom=@$DT_SBOM_FILE"
```
