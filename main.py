
import cv2

# Input and output video paths
input_video = "input.mp4"
output_video = "output.mp4"

# Open the input video
cap = cv2.VideoCapture(input_video)

# Check whether the video opened successfully
if not cap.isOpened():
    print("Error: Could not open input video.")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set up the output video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    output_video, fourcc, fps, (width, height)
)

frame_number = 0

# Read and process every frame
while True:
    ret, frame = cap.read()

    # Stop when no more frames are available
    if not ret:
        break

    frame_number += 1

    # Draw a green rectangle on each frame
    cv2.rectangle(
        frame,
        (50, 50),
        (width - 50, height - 50),
        (0, 255, 0),
        2
    )

    # Draw text on each frame
    cv2.putText(
        frame,
        f"Frame: {frame_number}",
        (60, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Save the processed frame
    out.write(frame)

# Release resources
cap.release()
out.release()

print("Video processing completed!")
print(f"Output saved as: {output_video}")
