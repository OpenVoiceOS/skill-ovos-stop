# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from mycroft.skills.core import FallbackSkill, intent_handler
from ovos_utils.process_utils import RuntimeRequirements
from ovos_utils import classproperty


class StopSkill(FallbackSkill):

    def initialize(self):
        self.register_fallback(self.handle_fallback, 80)

    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(internet_before_load=False,
                                   network_before_load=False,
                                   gui_before_load=False,
                                   requires_internet=False,
                                   requires_network=False,
                                   requires_gui=False,
                                   no_internet_fallback=True,
                                   no_network_fallback=True,
                                   no_gui_fallback=True)

    @intent_handler("stop.intent")
    def handle_stop(self, message):
        self.bus.emit(message.reply("mycroft.stop", {}))

    def handle_fallback(self, message):
        utterance = message.data.get("utterance", "")
        if self.voc_match(utterance, 'StopKeyword'):
            self.bus.emit(message.reply("mycroft.stop", {}))
            return True
        return False


def create_skill():
    return StopSkill()
