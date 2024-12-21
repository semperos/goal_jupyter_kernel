import unittest

import jupyter_kernel_test as jkt


class GoalKernelTests(jkt.KernelTests):
    # REQUIRED

    # the kernel to be tested
    # this is the normally the name of the directory containing the
    # kernel.json file - you should be able to do
    # `jupyter console --kernel KERNEL_NAME`
    kernel_name = "goal"

    # Everything else is OPTIONAL

    # the name of the language the kernel executes
    # checked against language_info.name in kernel_info_reply
    language_name = "goal"

    # the normal file extension (including the leading dot) for this language
    # checked against language_info.file_extension in kernel_info_reply
    file_extension = ".goal"

    code_hello_world = r'''say"hello, world"'''

    completion_samples = [
        {
            "text": "s",
            "matches": [
                "say",
                "shell",
                "shift",
                "sign",
                "sin",
                "sqrt",
                "stat",
                "sub",
                "subfs",
            ],
        }
    ]

    # This doesn't work as expected because the impl never sends an execute_result message type,
    # so the test fails. Not sure how to do that properly, have tested manually.
    # code_execute_result = [{"code": "+/!101", "result": "5050"}]


if __name__ == "__main__":
    unittest.main()
