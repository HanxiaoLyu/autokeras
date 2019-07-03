import numpy as np
import tensorflow as tf
from autokeras.auto.processor import ImageAugment


def test_image_augment_cifar10():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    raw_data = x_train
    image_augmenter = ImageAugment()
    augmented_data = image_augmenter.transform(x_train=raw_data,
                                               rotation_range=1,
                                               random_crop_width=1,
                                               random_crop_height=2,
                                               random_crop_seed=3,
                                               brightness_range=0.4,
                                               saturation_range=0.2,
                                               horizontal_flip=True,
                                               vertical_flip=True,
                                               translation_bottom=1,
                                               translation_top=2,
                                               translation_right=1,
                                               translation_left=2,
                                               gaussian_noise=True
                                               )
    assert augmented_data.shape == raw_data.shape

def test_image_augment_mnist():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    shape = np.array(x_train).shape
    raw_data = tf.reshape(x_train,[shape[0],shape[1],shape[2],1])
    image_augmenter = ImageAugment()
    augmented_data = image_augmenter.transform(x_train=raw_data,
                                               rotation_range=1,
                                               random_crop_width=1,
                                               random_crop_height=2,
                                               random_crop_seed=3,
                                               brightness_range=0.4,
                                               saturation_range=0.2,
                                               horizontal_flip=True,
                                               vertical_flip=True,
                                               translation_bottom=1,
                                               translation_top=2,
                                               translation_right=1,
                                               translation_left=2,
                                               gaussian_noise=True
                                               )
    assert augmented_data.shape == raw_data.shape
    
def test_image_augment_self_defined_data():
    x_train = np.random.rand(1000,50,49,2)
    raw_data = x_train
    image_augmenter = ImageAugment()
    augmented_data = image_augmenter.transform(x_train=raw_data,
                                               rotation_range=1,
                                               random_crop_width=1,
                                               random_crop_height=2,
                                               random_crop_seed=3,
                                               brightness_range=0.4,
                                               saturation_range=0.2,
                                               horizontal_flip=True,
                                               vertical_flip=True,
                                               translation_bottom=1,
                                               translation_top=2,
                                               translation_right=1,
                                               translation_left=2,
                                               gaussian_noise=True
                                               )
    assert augmented_data.shape == raw_data.shape
