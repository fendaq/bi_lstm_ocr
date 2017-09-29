class TrainConfig:
    def __init__(self):
        self.batch_size = 50
        self.log_dir = 'log/'
        self.is_restore = False
        self.checkpoint_dir = 'checkpoint/'
        self.num_epochs = 5
        self.save_steps = 1
        self.validation_steps = 5
        self.charset_file = "C:/Users/asus.11/Documents/Deep Learning/ocr playground/chars.txt"
