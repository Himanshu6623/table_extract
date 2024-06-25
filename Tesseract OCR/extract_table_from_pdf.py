import tabula
pdf_path='https://acrobat.adobe.com/id/urn:aaid:sc:AP:31d8c83c-ea14-4fbb-af48-e2041a340a68'
df=tabula.read_pdf(pdf_path,pages='1')
print(df[0])