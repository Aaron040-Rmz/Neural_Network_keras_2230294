from src.keras_2 import train_image_detection_model

def main():

    model_image = train_image_detection_model()
    print(model_image)
    
   
if __name__ == "__main__":
    main()