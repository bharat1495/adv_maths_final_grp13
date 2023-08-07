import streamlit as st
from PIL import Image
from ultralytics import YOLO


# Load the YOLOv5 model
model = YOLO('models/yolov8/best.pt')
names = model.names
def predict(image):
    # Perform object detection on the input image
    results = model.predict(image)
    return results

def main():
    st.set_page_config(page_title="Object Detection", layout="wide")

    st.title("YOLOv8 Signal Detection")
    st.write("Upload an image to detect objects.")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=False)

        if st.button("Detect Objects"):
            # Perform object detection using YOLOv5 model
            results = predict(image)
            # Show the results
            for r in results:
                
                im_array = r.plot()  # plot a BGR numpy array of predictions
                im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
                st.image(im,use_column_width=False)  # show image
                try:
                    for c in r.boxes.cls:
                        st.write(names[int(c)])
                except Exception as e:
                    print(e)
                    pass
            # The 'results' object contains the detected objects and their bounding box coordinates.

if __name__ == "__main__":
    main()
