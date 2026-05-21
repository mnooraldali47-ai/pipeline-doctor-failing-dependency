# failing-dependency

## Zweck
Testfall für Pipeline Doctor: **Build schlägt in der Install-Stage fehl.**

## Erwarteter Fehler
```
ERROR: Could not find a version that satisfies the requirement
       this-package-does-not-exist-12345==1.0
ERROR: No matching distribution found for this-package-does-not-exist-12345==1.0
```

## Fehler-Typ
`pip install` — nicht existierendes Paket in `requirements.txt`

## Stage die fehlschlägt
`Install Dependencies` — Stage `Test` wird nie erreicht.
