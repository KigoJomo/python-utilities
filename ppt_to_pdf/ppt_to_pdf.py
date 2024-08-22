import os
import comtypes.client

def convert_ppt_to_pdf(ppt_path, pdf_path):
    # Initialize PowerPoint application
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1  # Make PowerPoint visible for debugging

    try:
        # Open the PowerPoint file
        presentation = powerpoint.Presentations.Open(ppt_path)

        # Save as PDF
        presentation.SaveAs(pdf_path, FileFormat=32)  # 32 is the FileFormat for PDF

        # Close the presentation
        presentation.Close()
    except Exception as e:
        print(f"Error converting {ppt_path}: {e}")
    finally:
        # Quit PowerPoint application
        powerpoint.Quit()

def convert_all_ppts_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.ppt', '.pptx')):
            ppt_path = os.path.join(folder_path, filename)
            pdf_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.pdf")
            print(f"Converting {ppt_path} to {pdf_path}")
            convert_ppt_to_pdf(ppt_path, pdf_path)

if __name__ == "__main__":
    # Set the folder path containing the PowerPoint files
    folder_path = r"C:\Users\Nova\Documents\BSc-IT-3.1\Design and Analysis of Algorithms\Notes\convert"

    convert_all_ppts_in_folder(folder_path)