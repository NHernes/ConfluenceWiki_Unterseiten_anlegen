from tokenize import Name
import requests
import csv
import json
from requests.auth import HTTPBasicAuth
import datetime

#Authentifizierung zum Handshake
try:
  f = open("authentication.txt", "r")
  auth_token=f.read()
  print(auth_token)

except:
  print("Benötigt wird ein Personal Access Token. Ihr könnt euch diesen hier generieren: https://wikis.fu-berlin.de/plugins/personalaccesstokens/usertokens.action")
  auth_token=input("Auth Token: ")
  f= open("authentication.txt","w+")
  f.write(auth_token)



#Inhalt der Hauptprüfungsseite
def unterseite_hk():
    body1="""
        <p class="auto-cursor-target">
  <br/>
</p>
<ac:structured-macro ac:macro-id="86d89334-7eef-428c-8a56-d945c1205608" ac:name="section" ac:schema-version="1">
  <ac:parameter ac:name="border">true</ac:parameter>
  <ac:rich-text-body>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <ac:structured-macro ac:macro-id="06a29ea9-4fcb-4878-b110-a6605a672662" ac:name="column" ac:schema-version="1">
      <ac:parameter ac:name="width">50%</ac:parameter>
      <ac:rich-text-body>
        <p>
          <strong>Allgemeine Informationen zur Prüfung</strong>
        </p>
        <p class="auto-cursor-target">
          <br/>
        </p>
        <table class="relative-table wrapped" style="width: 100%;">
          <colgroup> <col style="width: 29.9875%;"/> <col style="width: 69.9377%;"/> </colgroup>
          <tbody>
            <tr>
              <td colspan="1">Bearbeiter:in</td>
              <td colspan="1">
                <div class="content-wrapper">
                  <ac:task-list>
<ac:task>
<ac:task-id>2233</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                        <span class="placeholder-inline-tasks">
                          <ac:link>
                            <ri:user ri:userkey="ff8080824637ba01014637baa7630b13"/>
                          </ac:link> Word-Vorlage bis zum: <time datetime=""" + Vorlage_A_neu + """/></span>
                      </ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>3292</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                        <span class="placeholder-inline-tasks">
                          <ac:link>
                            <ri:user ri:userkey="ff8080824637ba01014637baa7630b13"/>
                          </ac:link> TN-Liste bis zum: <time datetime=""" + Teil_A_neu + """/></span>
                      </ac:task-body>
</ac:task>
</ac:task-list>
                </div>
              </td>
            </tr>
            <tr>
              <td>Name der Prüfung:</td>
              <td>
                <p>"""+ Prüfungsname + """</p>
              </td>
            </tr>
            <tr>
              <td>Datum + Uhrzeit:</td>
              <td>
                <div class="content-wrapper">
                  <p>"""+ datum_A + """</p>
                  <p>""" + Uhrzeit_A + """</p>
                </div>
              </td>
            </tr>
            <tr>
              <td>Dozierende (+E-Mail): """ + Mail + """</td>
              <td>
                <p>
                  <br/>
                </p>
              </td>
            </tr>
            <tr>
              <td colspan="1">Open/Closed-Book:</td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">Besonderheiten:</td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
          </tbody>
        </table>
        <p class="auto-cursor-target">
          <br/>
        </p>
        <p class="auto-cursor-target">
          <br/>
        </p>
      </ac:rich-text-body>
    </ac:structured-macro>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <p class="auto-cursor-target">
      <br/>
    </p>
            <p class="auto-cursor-target">
      <br/>
    </p>
    <ac:structured-macro ac:macro-id="2575ba19-dc4d-4de6-a85e-35cbccd6e937" ac:name="column" ac:schema-version="1">
      <ac:parameter ac:name="width">50%</ac:parameter>
      <ac:rich-text-body>
        <p>
          <strong>Prüfungsstatus</strong>
        </p>
        <table class="wrapped relative-table" style="width: 99.9363%;">
          <colgroup>
            <col style="width: 20.4953%;"/>
            <col style="width: 27.5509%;"/>
            <col style="width: 18.2157%;"/>
            <col style="width: 33.7887%;"/>
          </colgroup>
          <tbody>
            <tr>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <strong>Bearbeiter:in</strong>
              </td>
              <td colspan="1">
                <strong>Kommentar</strong>
              </td>
            </tr>
            <tr>
              <td rowspan="2">
                <em>
                  <strong>1. Unterlagen</strong>
                </em>
              </td>
              <td>
                <div class="content-wrapper">
                  <ac:task-list>
<ac:task>
<ac:task-id>2995</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>TN-Liste liegt vor</ac:task-body>
</ac:task>
</ac:task-list>
                </div>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <div class="content-wrapper">
                  <ac:task-list>
<ac:task>
<ac:task-id>3286</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>Aufgaben liegen vor</ac:task-body>
</ac:task>
</ac:task-list>
                </div>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td rowspan="2">
                <strong>
                  <em>2. Bearbeitung</em>
                </strong>
              </td>
              <td>
                <ac:task-list>
<ac:task>
<ac:task-id>2997</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>E-Exam erstellt</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3287</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>TN hochgeladen</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td rowspan="3">
                <strong>
                  <em>3. Qualitätskontrolle</em>
                </strong>
              </td>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>2999</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">Abnahme (intern)</span>
                    </ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3288</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">Prüfungseinsicht an Dozierenden kommuniziert</span>
                    </ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3289</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">Logins versendet</span>
                    </ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td rowspan="2">
                <strong>
                  <em>
                    <span class="placeholder-inline-tasks">4. </span>Finalisierung</em>
                </strong>
              </td>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3001</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>Abnahme durch Dozierende</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3290</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">finale Freigabe der Accounts</span>
                      <ac:emoticon ac:name="warning"/> (Nur bei EEC Prüfung)</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
          </tbody>
        </table>
        <p class="auto-cursor-target">
          <br/>
        </p>
      </ac:rich-text-body>
    </ac:structured-macro>
    <p class="auto-cursor-target">
      <br/>
    </p>
  </ac:rich-text-body>
</ac:structured-macro>
<p class="auto-cursor-target">
  <br/>
</p>
<ac:structured-macro ac:macro-id="05eabe83-a320-4119-96c7-f8902e77c16c" ac:name="section" ac:schema-version="1">
  <ac:parameter ac:name="border">true</ac:parameter>
  <ac:rich-text-body>
    <p class="auto-cursor-target">
      <br/>
    </p>
            <ac:structured-macro ac:macro-id="4808ef75-39c0-4110-b5f9-312b19d37afe" ac:name="column" ac:schema-version="1">
            <ac:parameter ac:name="width">50%</ac:parameter>
            <ac:rich-text-body>
                <p>
                <strong>Informationen für die Durchführung</strong>
                </p>
                <table class="relative-table wrapped" style="width: 51.7339%;">
                <colgroup>
                    <col style="width: 26.4026%;"/>
                    <col style="width: 73.5974%;"/>
                </colgroup>
                <tbody>
                    <tr>
                    <td>Lizenz:</td>
                    <td></td>
                    </tr>
                    <tr>
                    <td>Name Katalog:</td>
                    <td>
                        <p></p>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1"></td>
                    <td colspan="1"></td>
                    </tr>
                    <tr>
                    <td>
                        <p>Studis informiert:</p>
                    </td>
                    <td>-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Webexraum:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Uhrzeit für Dozent+CeDiS:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Uhrzeit für Studies:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Anzahl der gemeldeten TN:</td>
                    <td colspan="1">P: """ + Anzahl +"""</td>
                    </tr>
                    <tr>
                    <td colspan="1">Prüfungszeit: """ + Prüfungsdauer + """</td>
                    <td colspan="1"></td>
                    </tr>
                    <tr>
                    <td colspan="1">Nachteilsausgleiche:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Status Randomisierung:</td>
                    <td colspan="1">-</td>
                    </tr>
                </tbody>
                </table>
                <p class="auto-cursor-target">
                <br/>
                </p>
            </ac:rich-text-body>
            </ac:structured-macro>
            <p class="auto-cursor-target">
            <br/>
            </p>
            <ac:structured-macro ac:macro-id="a531722b-e066-414a-87df-3b711b5fc321" ac:name="column" ac:schema-version="1">
            <ac:parameter ac:name="width">50%</ac:parameter>
            <ac:rich-text-body>
                <p>
                <strong>Prüfungserstellung &amp; Qualitätskontrolle</strong>
                </p>
                <p>Prüfung erstellt von:</p>
                <p>Qualitätskontrolliert von:</p>
                <table class="wrapped">
                <colgroup>
                    <col/>
                    <col/>
                    <col/>
                </colgroup>
                <tbody>
                    <tr>
                    <th colspan="1">
                        <br/>
                    </th>
                    <th>Erstellung</th>
                    <th>QK</th>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <strong>Editor</strong>
                    </td>
                    <td>
                        <br/>
                    </td>
                    <td>
                        <br/>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>(optional) Ordinal-Skalen</p>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2119</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2151</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>(optional) wurde Layout übernommen und Punkte entfernt?</p>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2120</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2152</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Bepunktung kontrolliert</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2153</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2154</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Multiple-Choice Aufgaben überprüft</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2155</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2156</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Bepunktung kontrolliert</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2157</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2158</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Wiki-Link eingefügt</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2159</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2160</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Abschließende Kontrolle Editor/Plattform durchgeführt</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2161</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2162</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <strong>Plattform</strong>
                    </td>
                    <td colspan="1">
                        <p>
                        <br/>
                        </p>
                    </td>
                    <td colspan="1">
                        <p>
                        <br/>
                        </p>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Richtige Zeit eingestellt</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2165</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2166</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Richtige Vorlagenauswahl getroffen</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2167</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2168</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Design-Optionen hinzugefügt</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2169</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2170</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Multiple-Choice-Einstellungen gesetzt</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2171</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2172</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Reportmappe erstellt</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2173</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2174</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Dozierende freigeschaltet</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2175</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2176</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Dozierende + Sys-Admins in Nachbewertung eingetragen</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2177</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2178</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Reihenfolge der Fächer kontrolliert</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2191</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2192</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                </tbody>
                </table>
                <p class="auto-cursor-target">
                <br/>
                </p>
            </ac:rich-text-body>
            </ac:structured-macro>
            <p class="auto-cursor-target">
            <br/>
            </p>
        </ac:rich-text-body>
        </ac:structured-macro>
        <p class="auto-cursor-target">
        <ac:structured-macro ac:macro-id="8e101ad5-cacb-492b-8146-f6801bb69dc2" ac:name="attachments" ac:schema-version="1"/>
        </p>

    """
    return body1

#Inhalt der Nachprüfungsseite
def unterseite_nk():
    body3="""
        <p class="auto-cursor-target">
  <br/>
</p>
<ac:structured-macro ac:macro-id="86d89334-7eef-428c-8a56-d945c1205608" ac:name="section" ac:schema-version="1">
  <ac:parameter ac:name="border">true</ac:parameter>
  <ac:rich-text-body>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <ac:structured-macro ac:macro-id="06a29ea9-4fcb-4878-b110-a6605a672662" ac:name="column" ac:schema-version="1">
      <ac:parameter ac:name="width">50%</ac:parameter>
      <ac:rich-text-body>
        <p>
          <strong>Allgemeine Informationen zur Prüfung</strong>
        </p>
        <p class="auto-cursor-target">
          <br/>
        </p>
        <table class="relative-table wrapped" style="width: 100%;">
          <colgroup> <col style="width: 29.9875%;"/> <col style="width: 69.9377%;"/> </colgroup>
          <tbody>
            <tr>
              <td colspan="1">Bearbeiter:in</td>
              <td colspan="1">
                <div class="content-wrapper">
                  <ac:task-list>
<ac:task>
<ac:task-id>2233</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                        <span class="placeholder-inline-tasks">
                          <ac:link>
                            <ri:user ri:userkey="ff8080824637ba01014637baa7630b13"/>
                          </ac:link> Word-Vorlage bis zum: <time datetime=""" + Vorlage_B_neu + """/></span>
                      </ac:task-body>
</ac:task>
<ac:task>
<ac:task-id>3292</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                        <span class="placeholder-inline-tasks">
                          <ac:link>
                            <ri:user ri:userkey="ff8080824637ba01014637baa7630b13"/>
                          </ac:link> TN-Liste bis zum: <time datetime=""" + Teil_B_neu + """/></span>
                      </ac:task-body>
</ac:task>
</ac:task-list>
                </div>
              </td>
            </tr>
            <tr>
              <td>Name der Prüfung:</td>
              <td>
                <p>"""+ Prüfungsname + """</p>
              </td>
            </tr>
            <tr>
              <td>Datum + Uhrzeit:</td>
              <td>
                <div class="content-wrapper">
                  <p>"""+ datum_B + """</p>
                  <p>""" + Uhrzeit_B + """</p>
                </div>
              </td>
            </tr>
            <tr>
              <td>Dozierende (+E-Mail): """ + Mail + """</td>
              <td>
                <p>
                  <br/>
                </p>
              </td>
            </tr>
            <tr>
              <td colspan="1">Open/Closed-Book:</td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">Besonderheiten:</td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
          </tbody>
        </table>
        <p class="auto-cursor-target">
          <br/>
        </p>
        <p class="auto-cursor-target">
          <br/>
        </p>
      </ac:rich-text-body>
    </ac:structured-macro>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <p class="auto-cursor-target">
      <br/>
    </p>
    <p class="auto-cursor-target">
      <br/>
    </p>
            <p class="auto-cursor-target">
      <br/>
    </p>
    <ac:structured-macro ac:macro-id="2575ba19-dc4d-4de6-a85e-35cbccd6e937" ac:name="column" ac:schema-version="1">
      <ac:parameter ac:name="width">50%</ac:parameter>
      <ac:rich-text-body>
        <p>
          <strong>Prüfungsstatus</strong>
        </p>
        <table class="wrapped relative-table" style="width: 99.9363%;">
          <colgroup>
            <col style="width: 20.4953%;"/>
            <col style="width: 27.5509%;"/>
            <col style="width: 18.2157%;"/>
            <col style="width: 33.7887%;"/>
          </colgroup>
          <tbody>
            <tr>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <strong>Bearbeiter:in</strong>
              </td>
              <td colspan="1">
                <strong>Kommentar</strong>
              </td>
            </tr>
            <tr>
              <td rowspan="2">
                <em>
                  <strong>1. Unterlagen</strong>
                </em>
              </td>
              <td>
                <div class="content-wrapper">
                  <ac:task-list>
<ac:task>
<ac:task-id>2995</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>TN-Liste liegt vor</ac:task-body>
</ac:task>
</ac:task-list>
                </div>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <div class="content-wrapper">
                  <ac:task-list>
<ac:task>
<ac:task-id>3286</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>Aufgaben liegen vor</ac:task-body>
</ac:task>
</ac:task-list>
                </div>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td rowspan="2">
                <strong>
                  <em>2. Bearbeitung</em>
                </strong>
              </td>
              <td>
                <ac:task-list>
<ac:task>
<ac:task-id>2997</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>E-Exam erstellt</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3287</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>TN hochgeladen</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td rowspan="3">
                <strong>
                  <em>3. Qualitätskontrolle</em>
                </strong>
              </td>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>2999</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">Abnahme (intern)</span>
                    </ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3288</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">Prüfungseinsicht an Dozierenden kommuniziert</span>
                    </ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3289</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">Logins versendet</span>
                    </ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td rowspan="2">
                <strong>
                  <em>
                    <span class="placeholder-inline-tasks">4. </span>Finalisierung</em>
                </strong>
              </td>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3001</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>Abnahme durch Dozierende</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
            <tr>
              <td colspan="1">
                <ac:task-list>
<ac:task>
<ac:task-id>3290</ac:task-id>
<ac:task-status>incomplete</ac:task-status>
<ac:task-body>
                      <span class="placeholder-inline-tasks">finale Freigabe der Accounts</span>
                      <ac:emoticon ac:name="warning"/> (Nur bei EEC Prüfung)</ac:task-body>
</ac:task>
</ac:task-list>
              </td>
              <td colspan="1">
                <br/>
              </td>
              <td colspan="1">
                <br/>
              </td>
            </tr>
          </tbody>
        </table>
        <p class="auto-cursor-target">
          <br/>
        </p>
      </ac:rich-text-body>
    </ac:structured-macro>
    <p class="auto-cursor-target">
      <br/>
    </p>
  </ac:rich-text-body>
</ac:structured-macro>
<p class="auto-cursor-target">
  <br/>
</p>
<ac:structured-macro ac:macro-id="05eabe83-a320-4119-96c7-f8902e77c16c" ac:name="section" ac:schema-version="1">
  <ac:parameter ac:name="border">true</ac:parameter>
  <ac:rich-text-body>
    <p class="auto-cursor-target">
      <br/>
    </p>
            <ac:structured-macro ac:macro-id="4808ef75-39c0-4110-b5f9-312b19d37afe" ac:name="column" ac:schema-version="1">
            <ac:parameter ac:name="width">50%</ac:parameter>
            <ac:rich-text-body>
                <p>
                <strong>Informationen für die Durchführung</strong>
                </p>
                <table class="relative-table wrapped" style="width: 51.7339%;">
                <colgroup>
                    <col style="width: 26.4026%;"/>
                    <col style="width: 73.5974%;"/>
                </colgroup>
                <tbody>
                    <tr>
                    <td>Lizenz:</td>
                    <td></td>
                    </tr>
                    <tr>
                    <td>Name Katalog:</td>
                    <td>
                        <p></p>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1"></td>
                    <td colspan="1"></td>
                    </tr>
                    <tr>
                    <td>
                        <p>Studis informiert:</p>
                    </td>
                    <td>-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Webexraum:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Uhrzeit für Dozent+CeDiS:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Uhrzeit für Studies:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Anzahl der gemeldeten TN:</td>
                    <td colspan="1">P:</td>
                    </tr>
                    <tr>
                    <td colspan="1">Prüfungszeit: """ + Prüfungsdauer + """</td>
                    <td colspan="1"></td>
                    </tr>
                    <tr>
                    <td colspan="1">Nachteilsausgleiche:</td>
                    <td colspan="1">-</td>
                    </tr>
                    <tr>
                    <td colspan="1">Status Randomisierung:</td>
                    <td colspan="1">-</td>
                    </tr>
                </tbody>
                </table>
                <p class="auto-cursor-target">
                <br/>
                </p>
            </ac:rich-text-body>
            </ac:structured-macro>
            <p class="auto-cursor-target">
            <br/>
            </p>
            <ac:structured-macro ac:macro-id="a531722b-e066-414a-87df-3b711b5fc321" ac:name="column" ac:schema-version="1">
            <ac:parameter ac:name="width">50%</ac:parameter>
            <ac:rich-text-body>
                <p>
                <strong>Prüfungserstellung &amp; Qualitätskontrolle</strong>
                </p>
                <p>Prüfung erstellt von:</p>
                <p>Qualitätskontrolliert von:</p>
                <table class="wrapped">
                <colgroup>
                    <col/>
                    <col/>
                    <col/>
                </colgroup>
                <tbody>
                    <tr>
                    <th colspan="1">
                        <br/>
                    </th>
                    <th>Erstellung</th>
                    <th>QK</th>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <strong>Editor</strong>
                    </td>
                    <td>
                        <br/>
                    </td>
                    <td>
                        <br/>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>(optional) Ordinal-Skalen</p>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2119</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2151</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>(optional) wurde Layout übernommen und Punkte entfernt?</p>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2120</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td>
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2152</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Bepunktung kontrolliert</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2153</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2154</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Multiple-Choice Aufgaben überprüft</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2155</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2156</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Bepunktung kontrolliert</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2157</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2158</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Wiki-Link eingefügt</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2159</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2160</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Abschließende Kontrolle Editor/Plattform durchgeführt</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2161</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2162</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <strong>Plattform</strong>
                    </td>
                    <td colspan="1">
                        <p>
                        <br/>
                        </p>
                    </td>
                    <td colspan="1">
                        <p>
                        <br/>
                        </p>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">
                        <p>Richtige Zeit eingestellt</p>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2165</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2166</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Richtige Vorlagenauswahl getroffen</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2167</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2168</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Design-Optionen hinzugefügt</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2169</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2170</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Multiple-Choice-Einstellungen gesetzt</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2171</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2172</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Reportmappe erstellt</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2173</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2174</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Dozierende freigeschaltet</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2175</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2176</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Dozierende + Sys-Admins in Nachbewertung eingetragen</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2177</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2178</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                    <tr>
                    <td colspan="1">Reihenfolge der Fächer kontrolliert</td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2191</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    <td colspan="1">
                        <ac:task-list>
        <ac:task>
        <ac:task-id>2192</ac:task-id>
        <ac:task-status>incomplete</ac:task-status>
        <ac:task-body> </ac:task-body>
        </ac:task>
        </ac:task-list>
                    </td>
                    </tr>
                </tbody>
                </table>
                <p class="auto-cursor-target">
                <br/>
                </p>
            </ac:rich-text-body>
            </ac:structured-macro>
            <p class="auto-cursor-target">
            <br/>
            </p>
        </ac:rich-text-body>
        </ac:structured-macro>
        <p class="auto-cursor-target">
        <ac:structured-macro ac:macro-id="8e101ad5-cacb-492b-8146-f6801bb69dc2" ac:name="attachments" ac:schema-version="1"/>
        </p>

    """
    return body3

#Variable zum Hochzählen der angelegten Seite
x=0

#Öffnen CSV und beginnen des Einlesens
with open ('mailingliste.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter=';')
    line_count=0


#Definieren der Variablen aus der CSV
    for row in csv_reader:
                Mail=row['Mail']
                Name=row['Name']
                Prüfungsname=row['Prüfungsname']
                LVNummer=row['LVNummer']
                Prüfungsdauer=row['Pruefungsdauer']
                Anzahl=row['Anzahl']
                datum_A=row['datum_A']
                Uhrzeit_A=row['Uhrzeit_A']
                datum_B=row['datum_B']
                Uhrzeit_B=row['Uhrzeit_B']
                Vorlage_A=row['Vorlage_A']
                Teil_A=row['Teil_A']
                Vorlage_B=row['Vorlage_B']
                Teil_B=row['Teil_B']



# Hier werden die Informationen für die Hauptprüfung generiert
                #Datum wird in die Wiki-Schreibweise umgewandelt
                datum_A_neu=datetime.datetime.strptime(datum_A, '%d.%m.%Y').strftime('%Y-%m-%d')

                #Titel wird generiert
                seitennameA = "{} {} - HK ({})".format(datum_A_neu, Prüfungsname, Name, encoding="UTF-8")
                page_title = seitennameA

                #Daten zum Einreichen der Unterlagen werden angepasst, damit Sie im Wiki als Datumsfunktion erkannt werden
                Vorlage_A_neu=datetime.datetime.strptime(Vorlage_A, '%d.%m.%Y').strftime('%Y-%m-%d')
                Vorlage_A_neu = "\"{}\"".format(Vorlage_A_neu, encoding="UTF-8")

                Teil_A_neu=datetime.datetime.strptime(Teil_A, '%d.%m.%Y').strftime('%Y-%m-%d')
                Teil_A_neu = "\"{}\"".format(Teil_A_neu, encoding="UTF-8")

                #Funktion wird für das Generieren des Inhalts gerufen               
                page_html = unterseite_hk()



                #ID der Mutterseite
                parent_page_id = 1253344091

                #Name des gesamten Wiki-Bereichs
                space_key = 'eexam'

                #API-Website
                url = 'https://wikis.fu-berlin.de/rest/api/content/'

                # Request Headers
                headers = {
                'Content-Type': 'application/json;charset=iso-8859-1',
                "Authorization": "Bearer NzA4OTE2MjcxMjY2OuUZMcHzlpuaGII6N1QmZlRPaIbn"
                }
                # JSON Payload wird generiert
                data = {
                'type': 'page',
                'title': page_title,
                'ancestors': [{'id':parent_page_id}],
                'space': {'key':space_key},
                'body': {
                    'storage':{
                        'value': page_html,
                        'representation':'storage',
                    }
                }
                }

                #Hochzählen nach Anlegen der Seite, um beim Printen die Seitenzahl anzeigen zu können
                x=x+1

                #API Befehl wird ausgelöst
                try:

                    r = requests.post(url=url, data=json.dumps(data), headers=headers)

                    # Consider any status other than 2xx an error
                    if not r.status_code // 100 == 2:
                        print("Error: Unexpected response {}".format(r))
                    else:
                        seite = "Seite Nr {} angelegt".format(x)
                        print(seite)

                except requests.exceptions.RequestException as e:

                # A serious problem happened, like an SSLError or InvalidURL
                    print("Error: {}".format(e))

                #Nachprüfungsseite
                datum_B_neu=datetime.datetime.strptime(datum_B, '%d.%m.%Y').strftime('%Y-%m-%d')
                seitennameB = "{} {} - NK ({})".format(datum_B_neu, Prüfungsname, Name)

                page_title = seitennameB

                #Daten zum Einreichen der Unterlagen werden angepasst, damit Sie im Wiki als Datumsfunktion erkannt werden
                Vorlage_B_neu=datetime.datetime.strptime(Vorlage_B, '%d.%m.%Y').strftime('%Y-%m-%d')
                Vorlage_B_neu = "\"{}\"".format(Vorlage_B_neu, encoding="UTF-8")

                Teil_B_neu=datetime.datetime.strptime(Teil_B, '%d.%m.%Y').strftime('%Y-%m-%d')
                Teil_B_neu = "\"{}\"".format(Teil_B_neu, encoding="UTF-8")
                page_html = unterseite_nk()

                data = {
                'type': 'page',
                'title': page_title,
                'ancestors': [{'id':parent_page_id}],
                'space': {'key':space_key},
                'body': {
                    'storage':{
                        'value': page_html,
                        'representation':'storage',
                    }
                }
                }

                x=x+1
                
                try:

                    r = requests.post(url=url, data=json.dumps(data), headers=headers)

                    # Consider any status other than 2xx an error
                    if not r.status_code // 100 == 2:
                        print("Error: Unexpected response {}".format(r))
                    else:
                        seite = "Seite Nr {} angelegt".format(x)
                        print(seite)

                except requests.exceptions.RequestException as e:

                # A serious problem happened, like an SSLError or InvalidURL
                    print("Error: {}".format(e))