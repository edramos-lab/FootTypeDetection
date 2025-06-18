# Foot Type Detection Dataset

A YOLO-formatted dataset for foot type detection with automated label conversion utilities.

## Overview

This repository contains a dataset and tools for foot type detection using YOLO (You Only Look Once) object detection. The dataset has been processed to convert all annotations to a single class (class 0 - "present") for simplified detection tasks.

## Dataset Structure

```
foot-type-singleclass/
├── data.yaml                 # YOLO dataset configuration file
├── train/                    # Training data
│   ├── images/              # Training images
│   └── labels/              # Training annotations (YOLO format)
├── valid/                    # Validation data
│   ├── images/              # Validation images
│   └── labels/              # Validation annotations (YOLO format)
└── test/                     # Test data (if available)
    ├── images/              # Test images
    └── labels/              # Test annotations (YOLO format)
```

## Dataset Statistics

- **Training Images**: 1,000+ foot images
- **Validation Images**: 100+ foot images
- **Format**: YOLO format annotations
- **Classes**: Single class (0 - "present")
- **Image Types**: Various foot images from different angles and lighting conditions

## Files

### `main.py`
A Python script that converts all YOLO annotation files to use class ID 0 (present). This script:

- Processes all `.txt` annotation files in specified directories
- Converts all class IDs to 0
- Preserves bounding box coordinates (x_center, y_center, width, height)
- Skips malformed annotation lines
- Works with both training and validation datasets

#### Usage

```bash
python main.py
```

The script will automatically process:
- `/path/to/foot-type-singleclass/train/labels/`
- `/path/to/foot-type-singleclass/valid/labels/`

### `data.yaml`
YOLO dataset configuration file containing:
- Dataset paths
- Number of classes
- Class names
- Training/validation split information

## YOLO Annotation Format

Each annotation file contains one line per object in the following format:
```
class_id x_center y_center width height
```

Where:
- `class_id`: Always 0 (present)
- `x_center, y_center`: Normalized center coordinates (0-1)
- `width, height`: Normalized bounding box dimensions (0-1)

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/edramos-lab/FootTypeDetection.git
   cd FootTypeDetection
   ```

2. **Run the conversion script** (if needed):
   ```bash
   python main.py
   ```

3. **Use with YOLO training**:
   ```bash
   # Example with YOLOv8
   yolo train data=foot-type-singleclass/data.yaml model=yolov8n.pt epochs=100
   ```

## Dataset Characteristics

- **Single-class detection**: All foot instances are labeled as class 0
- **Diverse images**: Various foot types, angles, and lighting conditions
- **YOLO-compatible**: Ready for training with YOLO-based models
- **Pre-processed**: All annotations converted to consistent format

## Use Cases

- Foot type classification
- Podiatry applications
- Medical imaging analysis
- Computer vision research
- YOLO model training and evaluation

## Requirements

- Python 3.6+
- No additional dependencies required for the conversion script

## Contributing

Feel free to contribute by:
- Adding more foot images
- Improving annotation quality
- Enhancing the conversion script
- Adding additional utility functions

## License

This dataset is provided for research and educational purposes.

## Citation

If you use this dataset in your research, please cite:

```bibtex
@misc{foottypedetection2024,
  title={Foot Type Detection Dataset},
  author={edramos-lab},
  year={2024},
  url={https://github.com/edramos-lab/FootTypeDetection}
}
```

## Contact

For questions or issues, please open an issue on the GitHub repository. 