from client import ComplexDocumentOcrLayoutStructureExtractorClient

def main():
    client = ComplexDocumentOcrLayoutStructureExtractorClient()
    res = client.extract_document_layout_elements('sample_pdf_data')
    print('Complex Document OCR Layout Extractor: ' + res['document_extraction_id'])
    print('Pages: ' + str(res['pages_parsed_count']) + ' | Tables: ' + str(res['tabular_structures_extracted_count']))
    print('Top Node: ' + res['bounding_box_hierarchical_tree'][0]['type'] + ' ("' + res['bounding_box_hierarchical_tree'][0]['text'] + '")')
    print('Markdown URL: ' + res['structured_markdown_export_url'])

if __name__ == '__main__':
    main()
