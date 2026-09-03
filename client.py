class ComplexDocumentOcrLayoutStructureExtractorClient:
    def extract_document_layout_elements(self, raw_pdf_bytes_base64='JVBERi0xLjQKJ...', extract_tables_as_html=True):
        return {
            'document_extraction_id': 'doc_ocr_5519',
            'pages_parsed_count': 14,
            'tabular_structures_extracted_count': 4,
            'bounding_box_hierarchical_tree': [
                {'type': 'HEADER', 'text': 'Q4 Financial Balance Sheet', 'page': 1, 'bbox': [50, 80, 550, 110]},
                {'type': 'TABLE', 'rows': 8, 'cols': 4, 'page': 1, 'bbox': [50, 130, 550, 380]}
            ],
            'structured_markdown_export_url': 'https://docs.layout.genpark.ai/extractions/5519.md'
        }
