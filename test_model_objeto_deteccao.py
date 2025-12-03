# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import base64
from PIL import Image, ImageDraw

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file("/home/sobreiro/.oci/config", "functions-developer-profile")  # Provide the config file path

# Initialize service client with default config file
ai_vision_client = oci.ai_vision.AIServiceVisionClient(config)

# Preparing data
ocr_image = "foto.png"  # Provide the image location
with open(ocr_image, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())


# Send the request to service, some parameters are not required, see API
# doc for more info
analyze_image_response = ai_vision_client.analyze_image(
    analyze_image_details=oci.ai_vision.models.AnalyzeImageDetails(
        features=[
            oci.ai_vision.models.ImageObjectDetectionFeature(
                feature_type="OBJECT_DETECTION",
                max_results=50,
                model_id="ocid1.aivisionmodel.oc1.sa-saopaulo-1.amaaaaaakm2rzfqacwwa5w3xjy7xd5m6rdtojq4rgnsfh2rzdunbneeefhaa",
            )
        ],
        image=oci.ai_vision.models.InlineImageDetails(
            source="INLINE", data=encoded_string.decode("utf-8")
        ),
        compartment_id="ocid1.compartment.oc1..aaaaaaaav3se6eugwjeujk2exs6sf4uitigsl2iwaetkhrpdz7qocyxhonsq",
    ),
)

# Get the data from response
results = analyze_image_response.data

# Open the image
image = Image.open(ocr_image)
draw = ImageDraw.Draw(image)
width, height = image.size

# Draw bounding boxes
for obj in results.image_objects:
    vertices = obj.bounding_polygon.normalized_vertices
    shape = [(vertices[0].x * width, vertices[0].y * height), (vertices[2].x * width, vertices[2].y * height)]
    draw.rectangle(shape, outline="red", width=3)

# Save the image
image.save("foto_com_dano.png")

print("Imagem com os danos destacados salva em foto_com_dano.png")
