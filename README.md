# PDF to Markdown Converter

Ce programme Python utilise les bibliothèques `PyPDF2` et `markdownify` pour extraire du texte à partir de fichiers PDF et le convertir en format Markdown.

## Dépendances

Ce programme dépend des paquets Python suivants :

- `PyPDF2`
- `markdownify`

Vous pouvez les installer en utilisant pip :

```bash
pip install PyPDF2 markdownify
```

## Utilisation

Pour utiliser ce programme, exécutez la commande suivante dans votre terminal :

```bash
python3 pdf_to_markdown.py "<chemin_vers_le_pdf>"
```

Remplacez `<chemin_vers_le_pdf>` par le chemin vers le fichier PDF que vous souhaitez convertir. Le chemin peut être absolu ou relatif à l'emplacement du script Python.

## Limitations

Ce programme ne peut pas extraire le texte des images contenues dans les fichiers PDF. De plus, la conversion en Markdown peut ne pas préserver tous les détails de formatage si le texte du PDF est organisé de manière complexe.