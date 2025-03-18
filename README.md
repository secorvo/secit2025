# sec-it-2025 "Sichere Software-Entwicklung für Einsteiger:innen"

In diesem Repository sind Übungen und Lösungsideen für den Workshop "Sichere Software-Entwicklung für Einsteiger:innen" auf der secIT 2025 hinterlegt.

Wir wünschen viel Erfolg und vor allem viel Spaß!

## Zeitplan[^zeitplan]

| Zeit          | Thema                             |
| ------------- | --------------------------------- |
| 10:00 - 10:30 | Vorstellung                       |
| 10:30 - 11:00 | Einführung Hacking                |
| 11:00 - 11:45 | Spaß mit OWASP Juice Shop         |
| 11:45 - 12:30 | Spaß mit Github Secure Code Game  |
| 12:30 - 12:45 | Diskussion zu Hacking             |
| 12:45 - 13:30 | _Mittagspause_                    |
| 13:30 - 14:00 | Einführung Threat Modeling        |
| 14:00 - 14:45 | Spaß mit Threat Dragon            |
| 14:45 - 15:15 | Spaß mit pyTM                     |
| 15:15 - 15:30 | Diskussion zu Threat Modeling     |
| 15:30 - 15:45 | Einführung Secure Supply Chain    |
| 15:45 - 16:30 | Spaß mit SBOMs                    |
| 16:30 - 16:45 | Diskussion zu Secure Supply Chain |
| 16:45 - 17:00 | Zusammenfassung und Abschluss     |

[^zeitplan]: Pausen werden dynamisch gestaltet

## Trainingsumgebung

Die Trainingsumgebung ist eine virtuelle Maschine mit Kali-Linux, die über Deskmate bereitgestellt wird. Die Login-Daten werden zu Beginn des Workshops bereitgestellt.

[Secorvo @ Deskmate](https://secorvo.deskmate.me/)

### Optimierungsmöglichkeit

Ein kleiner Nachteil der Deskmate-Lösung ist die eingeschränkte Bedienung der GUI über den Browser. Vor allem funktioniert _Copy and Paste_ in dieser Umgebung nicht. Im Folgenden wird eine Möglichkeit vorgestellt, diesen Nachteil durch die Nutzung von SSH zu kompensieren.

#### Tailscale.com

Eine einfache Möglichkeit, die virtuellen Maschinen von Deskmate für einen externen Zugang zu öffnen bietet [Tailscale](https://tailscale.com/). Tailscale ist eine Verwaltungslösung um auf Basis der [Wireguard](https://www.wireguard.com/)-Technologie komfortabel ein Meshed-VPN aufzusetzen. Für kleine Umgebungen ist Tailscale kostenlos verfügbar. Zunächst muss man sich bei Tailscale anmelden sowie den eigenen Client mit der Tailscale-Software ausstatten und dort registrieren.

#### Tailscale auf dem Deskmate-Rechner

Auf dem Deskmate Rechner kann Tailscale einfach[^einfach] mit 

[^einfach]: Einfach ist natürlich nur sicher, wenn man sich vorher das Script angeschaut hat :wink:

```bash
curl -fsSL https://tailscale.com/install.sh | sudo sh
sudo tailscale up
```

installiert werden. Mit dem am Ende der Installation bereitgestellten Link kann man die Maschine bei Tailscale registrieren. Es empfiehlt sich, in der Admin-Konsole den Rechner ggf. umzubenennen (z. B. in `secit-deskmate`).

#### SSH auf dem Deskmate-Rechner

Auf einem Kali-Linux ist der SSH-Dienst deaktiviert. Dieser kann wie folgt aktiviert werden:

```bash
sudo dpkg-reconfigure openssh-server
sudo systemctl start ssh.service 
```

#### Anmeldung per SSH

Nach den Vorbereitungen kann man sich per `ssh` auf dem Deskmate-Rechner mit `ssh tpsse@secit-deskmate` (s. o.) anmelden. Ggf. richtet man noch Public-Key-Authentication ein.

