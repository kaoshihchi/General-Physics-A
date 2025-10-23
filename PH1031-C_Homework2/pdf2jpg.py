# Env: pdf2jpg
import fitz  # PyMuPDF
import os

def pdf_to_jpg():
    # Get current folder (where this script is located)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # List all PDF files
    pdf_files = [f for f in os.listdir(base_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in this folder.")
        return

    print(f"Found {len(pdf_files)} PDF(s). Starting conversion...\n")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(base_dir, pdf_file)
        pdf_name = os.path.splitext(pdf_file)[0]
        output_folder = os.path.join(base_dir, pdf_name)

        os.makedirs(output_folder, exist_ok=True)

        doc = fitz.open(pdf_path)
        print(f"Converting: {pdf_file} ({doc.page_count} pages)")

        for page_index in range(doc.page_count):
            page = doc.load_page(page_index)
            pix = page.get_pixmap(dpi=200)  # increase dpi for higher resolution
            output_path = os.path.join(output_folder, f"page_{page_index+1:03d}.jpg")
            pix.save(output_path)

        doc.close()
        print(f"Saved images to folder: {output_folder}\n")

    print("✅ All PDFs converted successfully!")


if __name__ == "__main__":
    try:
        import fitz
        if not (hasattr(fitz, "open") and "PyMuPDF" in (getattr(fitz, "__doc__", "") or "")):
            raise ImportError
    except ImportError:
        print("⚠️ Wrong 'fitz' module detected. Please run:\n"
              "pip uninstall fitz frontend\n"
              "pip install pymupdf\n")
    else:
        pdf_to_jpg()
